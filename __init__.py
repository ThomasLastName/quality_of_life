import warnings
def foo():
    warnings.warn(
        "This version is deprecated and no longer being maintaned! Please instead see https://github.com/ThomasLastName/quality-of-life",
        DeprecationWarning
    )

foo()
