import streamlit as st
import pandas as pd
from core.parser import CodeParser
from core.analyzer import Analyzer
from core.docstring_generator import DocstringGenerator
from core.validator import Validator
from core.metrics import Metrics

st.set_page_config(page_title="AI Reviewer", layout="wide")

# ---------- SIDEBAR ----------
st.sidebar.title("AI Reviewer")

st.sidebar.subheader("Upload File")
uploaded_file = st.sidebar.file_uploader("Upload Python file", type=["py"])

st.sidebar.subheader("Filters")
show_good = st.sidebar.checkbox("Show Good", True)
show_avg = st.sidebar.checkbox("Show Average", True)
show_poor = st.sidebar.checkbox("Show Poor", True)

run_btn = st.sidebar.button("Run Analysis")

st.sidebar.divider()
st.sidebar.info("Upload file and click Run Analysis")

# ---------- HEADER ----------
st.title("AI Code Review Dashboard")
st.caption("Smart Python Code Quality Analyzer")

st.divider()

# ---------- EMPTY STATE ----------
if not uploaded_file:
    st.info("Upload a Python file from sidebar to begin analysis")

    col1, col2, col3 = st.columns(3)
    col1.metric("Functions", 0)
    col2.metric("Classes", 0)
    col3.metric("Imports", 0)

    st.divider()

    st.subheader("System Status")
    st.success("Ready for Analysis")

# ---------- RUN ANALYSIS ----------
if uploaded_file and run_btn:

    with st.spinner("Analyzing code..."):

        with open("temp.py", "wb") as f:
            f.write(uploaded_file.read())

        parser = CodeParser("temp.py")
        analyzer = Analyzer(parser)
        docgen = DocstringGenerator()
        validator = Validator()
        metrics = Metrics()

        functions = parser.get_functions()
        classes = parser.get_classes()
        imports = parser.get_imports()

        # ---------- OVERVIEW ----------
        st.subheader("Overview")

        col1, col2, col3 = st.columns(3)
        col1.metric("Functions", len(functions))
        col2.metric("Classes", len(classes))
        col3.metric("Imports", len(imports))

        st.divider()

        # ---------- ISSUES ----------
        st.subheader("Detected Issues")

        issues = analyzer.detect_issues()

        if issues:
            for issue in issues:
                st.error(issue)
        else:
            st.success("No issues detected")

        st.divider()

        # ---------- FUNCTION ANALYSIS ----------
        st.subheader("Function Analysis")

        report_rows = []

        for func in functions:

            doc = docgen.generate(func)
            problems = validator.validate_docstring(doc)
            score = metrics.calculate_score(problems)

            # filtering
            if score > 80 and not show_good:
                continue
            if 50 < score <= 80 and not show_avg:
                continue
            if score <= 50 and not show_poor:
                continue

            with st.container(border=True):

                left, right = st.columns([4,1])

                with left:
                    st.markdown(f"### {func}")
                    st.code(doc, language="python")

                with right:
                    st.metric("Score", score)

                    if score > 80:
                        st.success("Good")
                    elif score > 50:
                        st.warning("Average")
                    else:
                        st.error("Poor")

                if problems:
                    st.warning("Issues: " + ", ".join(problems))
                else:
                    st.info("No problems found")

            report_rows.append({
                "Function": func,
                "Score": score,
                "Issues": ", ".join(problems) if problems else "None"
            })

        # ---------- REPORT TABLE ----------
        st.divider()
        st.subheader("Analysis Report")

        if report_rows:

            df = pd.DataFrame(report_rows)

            st.dataframe(df, use_container_width=True)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "Download Report CSV",
                csv,
                "analysis_report.csv",
                "text/csv"
            )
