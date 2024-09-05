# OSCAL REST API Definition

This is an open-source REST API specification for exchanging [OSCAL](https://pages.nist.gov/OSCAL/) content between tools and organizations.

The _OSCAL REST OpenAPI Specification_ addresses OSCAL XML, JSON and YAML content for all seven OSCAL models. Each OSCAL model has a primary set of REST API methods and endpoints for the OSCAL content itself, as well as methods and endpoints for snapshots and attachments. OSCAL profiles also have methods and endpoints for live profile resolution and snapshots of resolved profiles.

The _OSCAL REST OpenAPI Specification_ is expressed using [OpenAPI](https://www.openapis.org/) 3.1.

For more information, vist and bookmark [https://docs.oscal.io/docs/oscal-rest-openapi](https://docs.oscal.io/docs/oscal-rest-openapi)

## Conventions and Organization

All endpoint syntax is provided as:

| METHODS | ENDPOINTS |
|:--- |:--- |
| `GET`, `POST` | `/{model-name}`  |
| `GET`, `PUT`, `DELETE` | `/{model-name}/{content-uuid}` |
| `GET`, `POST` | `/{model-name}/{content-uuid}/attachment` |
| `GET`, `PUT`, `DELETE` | `/{model-name}/{content-uuid}/attachment/{resource-uuid}` |
| `GET`, `POST` | `/{model-name}/{content-uuid}/snapshot` |
| `GET`, `PUT`, `DELETE` | `{model-name}/{content-uuid}/snapshot/{snapshot-uuid}` |




The `{model-name}` is always one of the seven root-level OSCAL model names exactly as they are defined in the OSCAL syntax. Simply replace `{model-name}` with one of the following:

- `catalog`
- `profile`
- `component-definition`
- `system-security-plan`
- `assessment plan`
- `assessment-results`
- `plan-of-action-and-milestones`

Profiles have additional endpoints related to profile resolution:

| METHODS | ENDPOINTS |
|:--- |:--- |
| `GET` | `/profile/{content-uuid}/resolved-catalog`  |
| `GET`, `POST` | `/profile/{content-uuid}/resolved-snapshot` |
| `GET`, `PUT`, `DELETE` | `/{model-name}/{content-uuid}/resolved-snapshot-uuid` |


## Known Issue: XML Expression

There is a known OpenAPI issue that prevents proper definition of OSCAL XML schemas.

**When the specification calls for OSCAL content to be accepted or returned, the content must be fully valid OSCAL per the NIST standard, even if the specification shows a non-compliant schema or example.**

### Additional Information

All versions of the OpenAPI specification only accept JSON schema definitions, and attempts to derive any XML schema from the JSON schema.

The issue is JSON elements only have _children_, while XML elements have both _attributes_ and _children_. There is no way to specify an OSCAL XML element _attributes_ using a JSON schema. As a result all OpenAPI viewers and code generators incorrectly represent OSCAL XML element _attributes_ as element _children_.


## Viewing / Editing

The proposed OSCAL REST OpenAPI specification is expressed using the OpenAPI 3.1 standard:
[RAW](OSCALRestOpenAPI.json) | [VIEWER](https://raw.githack.com/EasyDynamics/oscal-rest/develop/viewer/index.html?url=https://raw.githubusercontent.com/EasyDynamics/oscal-rest/develop/OSCALRestOpenAPI.json)


## Contributing and Feedback

If you have feedback, please consider one of the following options:
- Add a comment to an [existing issue](https://github.com/EasyDynamics/oscal-rest/issues);
- If you don't see an appropriate existing issue, create a [new issue](https://github.com/EasyDynamics/oscal-rest/issues/new); or
- send a message to us: [oscal@oscal.io](mailto:oscal@oscal.io).

For the process of Contributing to the project, please review
[CONTRIBUTING.md](https://github.com/EasyDynamics/.github/blob/main/CONTRIBUTING.md)
and adhere to the [Code of Conduct](https://github.com/EasyDynamics/.github/blob/main/CODE_OF_CONDUCT.md).

## Licensing

For information on the project's license, please review the [LICENSE](/LICENSE) file.
