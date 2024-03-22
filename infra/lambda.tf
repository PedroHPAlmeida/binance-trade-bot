resource "aws_lambda_function" "lambda_function" {
  depends_on = [ aws_s3_object.handler_file ]

  function_name = "binance_trades"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "src.handler.handler"
  runtime       = "python3.10"

  s3_bucket = aws_s3_bucket.binance_trades_deployments.bucket
  s3_key    = var.DEPLOYMENT_FILE_ZIP

  environment {
    variables = {
      BINANCE_API_KEY      = var.BINANCE_API_KEY
      BINANCE_SECRET_KEY   = var.BINANCE_SECRET_KEY
      MONGO_CONNECT_STRING = var.MONGO_CONNECT_STRING
    }
  }
}
