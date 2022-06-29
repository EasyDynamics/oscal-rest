# Handling UUIDs in `POST` and `PUT` operations

## `PUT` vs `POST`

```mermaid
graph LR
  Init([Make a request]) --> Pref{Preference on UUID}
  Pref -->|Yes| PUT
  Pref -->|No| POST
```

## `POST`

When creating new objects, `POST` is the preferred option. The UUID of the new object
does not need to be specified, so `POST` should be used when there is no UUID preference.
If the UUID is specified in the body, an HTTP 409 error will be returned.

### Making a `POST` request

```mermaid
graph LR
  POST([POST]) --> UUID{Is UUID specified in body}
  UUID -->|Yes| Error([Error])
  UUID -->|No| Z[Create new resource<br/>and generate UUID]
```

## `PUT`

When creating new objects, `PUT` should only be used when there is a preferred value for
the UUID. Additionally, it can be used to update an existing object by replacing its entire
definition with an updated version. Currently, `PUT` is defined to include the UUID in the
request path and the request body, but it is not necessary to specify the UUID in the body.
If provided, the UUID in the body must match the UUID in the path, or else an HTTP 409
error will be returned. If an object with the specified UUID exists, the `PUT` request will
update the existing object. If no objects with the specified UUID exist, a new object will
be created with the provided UUID.

### Making a `PUT` request

```mermaid
graph LR
  PUT([PUT]) --> UUID{Is UUID specified in body}
  UUID -->|No| Exist
  UUID -->|Yes| UUIDMatch
  UUIDMatch{Does the body UUID<br/>match path UUID}
  UUIDMatch -->|No| Error([Error])
  UUIDMatch -->|Yes| Exist
  Exist{Does a resource with the<br/>UUID already exist}
  Exist -->|Yes| Update[Update matching resource]
  Exist -->|No| Create[Create new resource<br/>with given UUID]
```
