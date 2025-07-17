
# Finance Models Documentation

Welcome to the **Finance Models** project! This repository contains articles and models focused on macroeconomic and financial analysis. The documentation is built using MkDocs with the Material theme and hosted on GitHub Pages.

## Table of Contents
- [About the Project](#about-the-project)
- [Getting Started](#index)
- [Documentation Structure](#documentation-structure)
- [Deployment Process](#deployment-process)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About the Project

**Finance Models** aims to provide in-depth articles and models to support macroeconomic and financial analysis. The documentation covers topics such as:
- Model introductions
- Advanced usage guides
- Blog-style articles
- Tutorials for getting started

Visit the live documentation: [Finance Models Documentation](https://TheStatsProject.github.io/finance-models-docs/)

---

## Getting Started

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/TheStatsProject/finance-models-docs.git
   cd finance-models-docs
   ```

2. Install documentation dependencies:
   ```bash
   pip install sphinx sphinx_rtd_theme sphinxcontrib-images sphinxcontrib-mermaid sphinx_design sphinx_copybutton
   ```
   
   Or install from the requirements file:
   ```bash
   pip install -r docs/requirements.txt
   ```

3. Build the documentation:
   ```bash
   cd docs
   make html
   ```

4. View the documentation by opening `docs/build/html/index.html` in your browser.

---

## Documentation Development

The documentation is built using Sphinx with several extensions for enhanced functionality:

- **sphinx**: Core documentation framework
- **sphinx_rtd_theme**: Read the Docs theme
- **sphinxcontrib-images**: Enhanced image handling
- **sphinxcontrib-mermaid**: Mermaid diagram support
- **sphinx_design**: Bootstrap components for Sphinx
- **sphinx_copybutton**: Copy button for code blocks

To contribute to the documentation, make sure you have the required dependencies installed as shown in the Getting Started section above.
