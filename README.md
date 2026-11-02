# KhmerLens

A weekend-sized Khmer text analyzer project built with Python and Streamlit.

## Current status

This is a runnable project scaffold, not a completed NLP analyzer. The interface
accepts and previews text. Segmentation, part-of-speech tagging, and vocabulary
lookup are planned; no analysis is currently fabricated or shown.

## Windows / VS Code setup

1. Extract the ZIP and open the `khmerlens` folder in VS Code.
2. Install Python 3.11 or 3.12 if needed, plus the recommended VS Code extensions.
3. In the VS Code PowerShell terminal, run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

If you have Python 3.11 instead, use `py -3.11` in the first command.
Using the executable directly avoids PowerShell activation-policy problems.
Open the local URL printed by Streamlit. Stop the server with Ctrl+C.

Select `.venv` using **Python: Select Interpreter** in the command palette.
Press F5 to run the included Streamlit debug configuration after setup.

## macOS / Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```

## Git and GitHub

The ZIP includes a local `.git` repository on `main` and an initial scaffold
commit authored by Codex. There is no remote repository configured yet.
Set your own identity before making your commits:

```bash
git config user.name "YOUR NAME"
git config user.email "YOUR GITHUB EMAIL"
```

In VS Code's Source Control panel, choose **Publish Branch**, sign in to GitHub,
and select a private or public repository named `khmerlens`.

Alternatively, create an empty GitHub repository (without a README or license)
and run, replacing YOUR_USERNAME:

```bash
git remote add origin https://github.com/YOUR_USERNAME/khmerlens.git
git push -u origin main
```

If your extraction software omits `.git`, run `git init -b main`, then
`git add .` and `git commit -m "Initialize KhmerLens scaffold"` after setting
Git identity.

## Next milestones

- [ ] Verify `khmer-nltk` compatibility in a separate environment and inspect its license.
- [ ] Connect real word segmentation and part-of-speech predictions.
- [ ] Add color-coded labels and explain the tag set.
- [ ] Add a small reviewed vocabulary JSON file; show unavailable definitions honestly.
- [ ] Check a small set of reviewed sentences and document errors.
- [ ] Add screenshots and deploy a demo.

Keep NLP code separate from the interface when integration begins. Do not claim
model training, accuracy, or morphological analysis that has not been implemented
and evaluated. Dependencies currently use a version range; pin a tested environment
before deployment. NLP dependencies are intentionally deferred until compatibility
is verified.
