# rbac-python

## Endpoints
* `POST /v1/users`
```
{
    username: "alamin-mahamud",
    password: "simple-password",
  }
```
Response - 201 Created
```
{
  "result": "success",
  "id": 1
}
```


* `POST /v1/authenticate`
  ```
  {
    username: "alamin-mahamud",
    password: "simple-password",
  }
  ```

  Response - 200
  ```
  {
    token: "aksjfkasdjfkasdfdjkajj123.B41232132
    expired_at: "2019-01-05:00:00 UTC+06"
  }
  ```
* `GET /v1/refresh-token`
Response - 200
```
{
    token: "aksjfkasdjfkasdfdjkajj123.B41232132
    expired_at: "2019-01-06:00:00 UTC+06"
}
```
