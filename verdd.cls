% Written by Khalid Alnajjar (mokha)

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{verdd}[2020/01/01 v0.1 Verdd dictionary template]

% defining conditions
\newif\if@defaulttypesize
\@defaulttypesizetrue
\newif\if@defaultpaper
\@defaultpapertrue

% declaring options
% font declarations
\DeclareOption{10pt}{
  \@defaulttypesizefalse
  \PassOptionsToClass{10pt}{book}}
\DeclareOption{11pt}{
  \@defaulttypesizefalse
  \PassOptionsToClass{11pt}{book}}

% paper size declarations
\DeclareOption{a5paper}{
  \@defaultpaperfalse
  \PassOptionsToClass{a5paper}{book}}
\DeclareOption{b5paper}{
  \@defaultpaperfalse
  \PassOptionsToClass{b5paper}{book}}
\DeclareOption{letterpaper}{
  \@defaultpaperfalse
  \PassOptionsToClass{letterpaper}{book}}
\DeclareOption{legalpaper}{
  \@defaultpaperfalse
  \PassOptionsToClass{legalpaper}{book}}
\DeclareOption{executivepaper}{
  \@defaultpaperfalse
  \PassOptionsToClass{executivepaper}{book}}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\if@defaulttypesize
  \PassOptionsToClass{12pt}{book}
\fi
\if@defaultpaper
  \PassOptionsToClass{a4paper}{book}
\fi
\PassOptionsToClass{a4paper}{book}

% we want it to be a two sided book
\PassOptionsToClass{twoside}{book}
\ProcessOptions\relax
\LoadClass{book}

% required packages
% \RequirePackage[utf8]{inputenc}
% \RequirePackage[T1]{fontenc}
\RequirePackage{geometry}
\geometry{top=1.7cm, left=1.15cm, right=2.0cm, bottom=2.0cm,
              textwidth=11.3cm, textheight=17.5cm,
              headheight=1.3cm, headsep=0.4cm}

