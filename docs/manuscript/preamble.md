# LaTeX Preamble

This file contains LaTeX packages and commands that are automatically injected into the document compilation process.

> **Infrastructure Note**: This file is parsed by `infrastructure/rendering/latex_utils.py` and combined with the configuration output by `infrastructure/rendering/pdf_renderer.py` before final Pandoc execution to generate the physical PDF holding this text.

```latex
% Core mathematics
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{amsthm}

% Document layout
\usepackage{geometry}
% Compact preprint geometry: keep a small print-safe frame while using the
% page width for figures and dense conceptual tables.
\geometry{left=0.15in,right=0.15in,top=0.24in,bottom=0.24in}
\usepackage{float}
\usepackage{graphicx}

% Tables
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}

% Code listings
\usepackage{listings}

% Typography and formatting
\usepackage{microtype}
\usepackage{xcolor}

% The manuscript is intentionally information-dense. Keep the title page's
% explicit sizes intact while giving the body a compact, readable baseline.
\AtBeginDocument{%
  \fontsize{9.5pt}{11.3pt}\selectfont
  \setlength{\parskip}{0.28em}
  \setlength{\abovedisplayskip}{0.45em}
  \setlength{\belowdisplayskip}{0.45em}
}

% Cross-references and citations
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    allcolors=red
}
\usepackage[capitalise,noabbrev]{cleveref}
\usepackage{natbib}

% Use system font discovery for portable Unicode code listings.
\usepackage{fontspec}
\IfFontExistsTF{JuliaMono}
  {\setmonofont{JuliaMono}[Scale=MatchLowercase]}
  {\setmonofont{DejaVu Sans Mono}[Scale=MatchLowercase]}

% Math font for unicode-math: Latin Modern Math (TeX Live) has full BMP
% coverage including U+2223 (\mid), U+226A/226B (\ll/\gg), and the Greek/
% blackboard letters used in equations. Without an explicit \setmathfont,
% unicode-math falls back to lmroman text font which lacks several glyphs
% and emits "Missing character" warnings on every \mid in math mode.
\setmathfont{latinmodern-math.otf}
```
