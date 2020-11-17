(TeX-add-style-hook
 "dave3625-report-2020"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("IEEEtran" "conference")))
   (TeX-run-style-hooks
    "latex2e"
    "IEEEtran"
    "IEEEtran10")
   (LaTeX-add-bibliographies
    "final_report"))
 :latex)

