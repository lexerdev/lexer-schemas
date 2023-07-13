import setuptools

with open("VERSION") as istream:
    VERSION = istream.read().strip()


setuptools.setup(
    name="lexer_schemas",
    version=VERSION,
    description="Lexer API schemas",
    packages=[
        "lexer_schemas",
        "lexer_schemas.commerce_api",
        "lexer_schemas.marketing_api",
        "lexer_schemas.profile_api",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "pydantic[email]",
    ],
)
