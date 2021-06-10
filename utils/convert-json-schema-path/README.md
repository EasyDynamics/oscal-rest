# Overview

Node.js app that will convert [OSCAL JSON Schemas](https://github.com/usnistgov/OSCAL/tree/main/json/schema) references to other objects (`$ref` values) to references by path

This is intended to be a temporary workaround until either [Swagger supports OpenAPI v3.1](https://github.com/swagger-api/swagger-ui/issues/5891) or NIST's OSCAL tooling supports [generating JSON schemas with reference by path](https://github.com/usnistgov/metaschema/issues/160).

# Usage
You'll first need to install the dependencies:
```
npm install
```

The syntax of the command is:
```
node app.js <Ooscal-json-schema-url> <output-file>
```

For example:
```
node app.js https://raw.githubusercontent.com/usnistgov/OSCAL/v1.0.0/json/schema/oscal_catalog_schema.json ~/Desktop/oscal_catalog_schema.json
```