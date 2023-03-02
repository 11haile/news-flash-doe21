variable "host" {
  type = string
}

variable "token" {
  validation {
    base64decode = token
  }
}
