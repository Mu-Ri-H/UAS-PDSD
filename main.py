import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import streamlit as st

with st.echo("below"):
    from st_pages import Page, add_page_title, show_pages

    "## Declaring the pages in your app:"

    show_pages(
        [
            Page("dashboard.py", "Dashboard", "🏠"),
        ]
    )

    add_page_title()  # Optional method to add title and icon to current page