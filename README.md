# OSCAL REST API Definition

A draft proposal from [Easy Dynamics](https://www.easydynamics.com) of an [OpenAPI](https://www.openapis.org/) REST specification for interacting with [OSCAL](https://pages.nist.gov/OSCAL/) models.
    
## Viewing / Editing
You can use a Swagger Editor, [local](https://github.com/swagger-api/swagger-editor) (Docker works great) or [online](https://editor.swagger.io/?url=https://raw.githubusercontent.com/EasyDynamics/oscal-rest/develop/openapi.yaml) to view the specification:

![OSCSAL REST Swagger Screenshot](docs/resources/swagger-editor-oscal-screenshot.png)

## Linting & Testing
1. Install [`yamllint`](https://github.com/adrienverge/yamllint)
2. Run `yamllint -c lint.yaml .`
    - This will lint all `.yaml` files

## Contributing

For the process of Contributing to the project, please review [CONTRIBUTING.md](/CONTRIBUTING.md)
and adhere to the [Code of Conduct](/CODE_OF_CONDUCT.md).

## Licensing

For information on the project's license, please review the [LICENSE](/LICENSE) file.
