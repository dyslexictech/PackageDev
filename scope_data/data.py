# https://www.sublimetext.com/docs/3/scope_naming.html
# https://manual.macromates.com/en/language_grammars#naming_conventions
DATA = """
    comment
        line
            double-slash
            double-dash
            number-sign
            percentage
        block
            documentation

    constant
        numeric
            integer
            float
            hex
            octal
            complex
        character
            escape
        language
        other
            placeholder

    entity
        name
            class
                forward-decl
            struct
            enum
            union
            trait
            interface
            type
            function
                constructor
                destructor
            namespace
            constant
            label
            section
            tag
        other
            inherited-class
            attribute-name

    invalid
        illegal
        deprecated

    keyword
        control
            conditional
            import
        operator
            assignment
            arithmetic
            bitwise
            logical
            word
        other

    markup
        heading
        list
            numbered
            unnumbered
        bold
        italic
        underline
            link
        inserted
        deleted
        quote
        raw
            inline
            block
        other

    meta
        class
        struct
        enum
        union
        trait
        interface
        type
        function
            parameters
            return-type
        namespace
        preprocessor
        path
        function-call
        block
        braces
        group
        parens
        brackets
        generic
        tag
        paragraph
        toc-list
        sequence
        mapping
            key
            value
        annotation
        set

    punctuation
        definition
            string
                begin
                end
            comment
                begin
                end
            keyword
            generic
                begin
                end
            placeholder
                begin
                end
        section
            block
                begin
                end
            braces
                begin
                end
            group
                begin
                end
            parens
                begin
                end
            brackets
                begin
                end
            sequence
                begin
                end
            mapping
                begin
                end
            set
                begin
                end
        separator
            sequence
            mapping
                key-value
                pair
            decimal
        terminator
        accessor
            arrow
            dot
            double-colon
            fat-arrow
            colon
            backslash

    storage
        type
        modifier

    string
        quoted
            single
            double
            triple
            other
        unquoted
        regexp
        interpolated
        other

    support
        constant
        function
        module
        type
        class
        other

    variable
        language
        parameter
        function
        annotation
        other
            constant
            member
"""