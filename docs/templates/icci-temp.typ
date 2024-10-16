#let demonstration(proposition, dem) = [
    #emph(proposition)

    #underline([*Dem.*])
    #dem
    #sym.qed
]

#let exercise(proposition, des) = [
    #emph(proposition)

    #underline([*Desarrollo*.])
    #des
]

#let conf(
    title: none,
    theme: none,
    authors: (),
    course: none,
    professor: none,
    institution_logo: none,
    faculty_logo: none,
    department_logo: none,
    project_logo: none,
    doc
) = {
    // Title page and authors

    align(center, text(20pt)[*UNIVERSIDAD DE TARAPACÁ*])

    if (institution_logo != none) {
        align(
            center,
            image(institution_logo, width: 15%)
        )
    } 
    else {
        align(center)[IMAGE]
    }

    align(center, text(18pt)[*FACULTAD DE INGENIERÍA*])

    if (faculty_logo != none) {
        align(
            center,
            image(faculty_logo, width: 15%)
        )
    }
    else {
        align(center)[IMAGE]
    }

    align(center, text(16pt)[
        *DEPARTAMENTO DE INGENIERÍA EN COMPUTACIÓN E INFORMÁTICA*
    ])

    if (department_logo != none) {
        align(
            center,
            image(department_logo, width: 20%)
        )
    }
    else {
        align(center)[IMAGE]
    }

    align(center, text(16pt)[*#title*])
    align(center, text(16pt)[*#theme*])

    text(15pt)[
    #align(bottom + right,
        grid(
            columns: (40%),
            row-gutter: -1.5em,
            align(left, 
                [#underline([*Alumnos*])\ ]
                + for name in authors [
                    #name \
            ]),
            
            align(left)[\ \
                #underline([*Asignatura*]) \
                #course
            ],

            align(left)[\ \
                #underline([*Profesor(a)*]) \
                #professor
            ]
        )
    )]

    align(
        center,
        text(12pt)[Septiembre - 2024]
    )

    set par(justify: true)
    set heading(numbering: "1.1.1.a.")
    pagebreak()

    let head = grid(
            columns: (10%, 80%, 10%),
            align(
                left, 
                if (institution_logo != none) {
                    image(institution_logo, width: 65%)
                }
                else [INST. LOGO]
            ),
            align(center)[
                UNIVERSIDAD DE TARAPACÁ\
                FACULTAD DE INGENIERÍA\
                DEPARTAMENTO DE INGENIERÍA EN COMPUTACIÓN E INFORMÁTICA
            ],
            align(
                left, 
                if (department_logo != none) {
                    image(department_logo, width: 170%)
                }
                else [DEPT. LOGO]
            ),
    )

    let foot = grid(
        columns: (45%, 10%, 45%),
        align(left, text(10pt)[#course]),
        align(center, [\ #counter(page).display()])
    ) 

    set page(
        header: align(right, head),
        margin: (top: 8em),
        footer: foot,
    )

    show link: underline

    show heading: it => {
        if counter(heading).get() != (1,) and it.level == 1 {
            pagebreak()
            it
        } else if it.level == 1 or it.level == 2 {
            v(8pt)
            it
        } else {
            it
        }
    }

    show outline.entry.where(
        level: 1
    ): it => {
        v(12pt, weak: true)
        text(size: 12pt, strong(it))
    }

    counter(page).update(1)

    // Index
    outline(
        title: none,
        indent: auto,
        fill: none,
    )

    pagebreak()

    doc
}
