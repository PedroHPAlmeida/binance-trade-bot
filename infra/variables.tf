variable "BINANCE_API_KEY" {
  type      = string
  sensitive = true
}

variable "BINANCE_SECRET_KEY" {
  type      = string
  sensitive = true
}

variable "MONGO_CONNECT_STRING" {
  type      = string
  sensitive = true
}

variable "ECR_IMAGE_URI" {
  type      = string
  sensitive = false
}
