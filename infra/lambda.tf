resource "aws_lambda_function" "lambda_function" {
  function_name = "binance_trades"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "handler.handler"
  runtime       = "python3.10"

  image_uri = "255310614335.dkr.ecr.us-east-1.amazonaws.com/binance-trades-bot:latest"
  package_type = "Image"

  environment {
    variables = {
      BINANCE_API_KEY      = var.BINANCE_API_KEY
      BINANCE_SECRET_KEY   = var.BINANCE_SECRET_KEY
      MONGO_CONNECT_STRING = var.MONGO_CONNECT_STRING
    }
  }
}
