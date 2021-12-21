# primrosepy

The purpose of this repo is to serve as a template for creating good python
scientific utilities.

A good scientific package should:

 1. Be a proper package that can be uploaded to PyPi

 2. Be oth a module and a CLI tool

 3. Have composable, nested commands for the CLI.

 4. Be gradually typed through MyPy

 5. Be tested with unit testing, fuzz testing, and golden testing (for the UI)

 6. Have good documentation (Sphinx?)

 7. Have benchmarked performance (space and time)

 8. Be formatted with Black

 9. Be fast 

    This is a tricky one, since it depends on the application. Sometimes speed
    isn't critical, so we can just write pure python. When speed is critical,
    we can wrap C++ code wrapped with rbind11. Or use Cython. Or Numba. Maybe
    this should not be part of the template?

 10. Be version controlled with git and hosted on GitHub (yes, GitLab also exists)

 11. Have a continuous integration platform for testing (GitHub actions?)
