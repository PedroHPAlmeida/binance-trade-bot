resource "aws_s3_bucket" "binance_trades_deployments" {
  bucket        = "binance-trades-deployments"
  force_destroy = true
  tags = {
    Name = "BinanceTradesZIPs"
  }
}

resource "aws_s3_bucket_ownership_controls" "ownership_controls_s3" {
  bucket = aws_s3_bucket.binance_trades_deployments.id

  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "github_actions_acl" {
  bucket = aws_s3_bucket.binance_trades_deployments.id
  acl    = "private"
  depends_on = [
    aws_s3_bucket_ownership_controls.ownership_controls_s3
  ]
}

resource "aws_s3_object" "handler_file" {
  bucket = aws_s3_bucket.binance_trades_deployments.bucket
  key    = "handler.zip"
  source = "${path.module}/handler.zip"

  etag = filemd5("${path.module}/handler.zip")
}
