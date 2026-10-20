import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="DataBuddy AI",
    page_icon="📊",
    layout="wide"
)


# -----------------------------
# Custom styling
# -----------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f8fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 1.5rem;
        background: linear-gradient(120deg, #172554, #2563eb);
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
    }

    .hero p {
        color: #e0e7ff;
        font-size: 1.05rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    """
    <div class="hero">
        <h1>DataBuddy AI</h1>
        <p>
            Upload your data. Discover patterns.
            Turn raw data into useful insights.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.title("DataBuddy AI")
    st.caption("Your personal data analysis workspace")

    st.markdown("---")
    st.subheader("Getting Started")

    st.write("1. Upload a CSV file.")
    st.write("2. Explore your dataset.")
    st.write("3. Check data quality.")
    st.write("4. Visualize your data.")

    st.markdown("---")
    st.caption("Built with Python, Pandas and Streamlit")


# -----------------------------
# CSV file upload
# -----------------------------

st.subheader("Upload Your Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"],
    help="Select a CSV dataset from your computer."
)


if uploaded_file is None:
    st.info(
        "Upload a CSV file to begin your analysis."
    )

    st.markdown("### What you can explore")

    col1, col2, col3 = st.columns(3)

    col1.metric("Data Overview", "Explore")
    col2.metric("Data Quality", "Inspect")
    col3.metric("Visualizations", "Discover")

    st.stop()


# -----------------------------
# Read dataset
# -----------------------------

try:
    df = pd.read_csv(uploaded_file)

except (
    pd.errors.ParserError,
    UnicodeDecodeError,
    ValueError
):
    st.error(
        "Unable to read this CSV file. "
        "Please check its format and try again."
    )
    st.stop()

except Exception:
    st.error(
        "Something went wrong while reading the file. "
        "Please try another CSV file."
    )
    st.stop()


if df.empty:
    st.warning("This CSV file does not contain any data.")
    st.stop()

if len(df.columns) == 0:
    st.warning("No columns were found in the CSV file.")
    st.stop()


# -----------------------------
# Dataset overview
# -----------------------------

st.markdown("---")
st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rows", f"{len(df):,}")
col2.metric("Total Columns", f"{len(df.columns):,}")
col3.metric(
    "Missing Cells",
    f"{int(df.isna().sum().sum()):,}"
)
col4.metric(
    "Duplicate Rows",
    f"{int(df.duplicated().sum()):,}"
)


# -----------------------------
# Dataset preview
# -----------------------------

st.markdown("---")
st.subheader("Explore Your Data")

st.caption(
    f"Showing the first {min(100, len(df))} rows."
)

st.dataframe(
    df.head(100),
    use_container_width=True
)


# -----------------------------
# Data quality report
# -----------------------------

st.markdown("---")
st.subheader("Data Quality Report")

quality_df = pd.DataFrame({
    "Column": df.columns.astype(str),
    "Data Type": [
        str(dtype) for dtype in df.dtypes
    ],
    "Missing Values": [
        int(value) for value in df.isna().sum()
    ],
    "Missing (%)": [
        round(float(value), 2)
        for value in (
            df.isna().mean() * 100
        )
    ],
    "Unique Values": [
        int(value) for value in df.nunique()
    ]
})

st.dataframe(
    quality_df,
    use_container_width=True,
    hide_index=True
)


# -----------------------------
# Statistical summary
# -----------------------------

st.markdown("---")
st.subheader("Statistical Summary")

numeric_df = df.select_dtypes(include="number")

if not numeric_df.empty:
    st.dataframe(
        numeric_df.describe().round(2),
        use_container_width=True
    )
else:
    st.info(
        "No numeric columns were found "
        "for statistical analysis."
    )


# -----------------------------
# Data visualization
# -----------------------------

st.markdown("---")
st.subheader("Visualize Your Data")

if not numeric_df.empty:

    selected_column = st.selectbox(
        "Select a numeric column",
        options=numeric_df.columns.tolist()
    )

    chart_type = st.radio(
        "Choose visualization",
        options=["Histogram", "Box Plot"],
        horizontal=True
    )

    if chart_type == "Histogram":
        fig = px.histogram(
            df,
            x=selected_column,
            title=f"Distribution of {selected_column}",
            template="plotly_white"
        )

    else:
        fig = px.box(
            df,
            y=selected_column,
            title=f"Distribution of {selected_column}",
            template="plotly_white"
        )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.info(
        "Charts will be available when your "
        "dataset contains numeric columns."
    )


# -----------------------------
# Download analysis report
# -----------------------------

st.markdown("---")
st.subheader("Export Your Analysis")

report = quality_df.to_csv(index=False)

st.download_button(
    label="Download Data Quality Report",
    data=report,
    file_name="databuddy_quality_report.csv",
    mime="text/csv"
)

st.success(
    "Dataset analysis completed successfully!"
)