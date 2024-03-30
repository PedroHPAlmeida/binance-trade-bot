resource "aws_iam_openid_connect_provider" "gh_oidc" {
  url = "https://token.actions.githubusercontent.com"

  client_id_list = [
    "sts.amazonaws.com",
  ]

  thumbprint_list = ["cf23df2207d99a74fbe169e3eba035e633b65d94"]
}

resource "aws_iam_role" "gh_actions_role_oidc" {
  name = "gh_actions_role_oidc"
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Federated" : "${aws_iam_openid_connect_provider.gh_oidc.id}"
        },
        "Action" : "sts:AssumeRoleWithWebIdentity",
        "Condition" : {
          "StringEquals" : {
            "token.actions.githubusercontent.com:aud" : "sts.amazonaws.com"
          },
          "StringLike" : {
            "token.actions.githubusercontent.com:sub" : "repo:PedroHPAlmeida/binance-trade-bot:*"
          }
        }
      }
    ]
  })
}

data "aws_iam_policy_document" "data_policy" {
  statement {
    actions = [
      "ecr:UploadLayerPart",
      "ecr:BatchGetImage",
      "ecr:BatchCheckLayerAvailability",
      "ecr:CompleteLayerUpload",
      "ecr:GetDownloadUrlForLayer",
      "ecr:InitiateLayerUpload",
      "ecr:PutImage"
    ]
    resources = [aws_ecr_repository.ecr_repository_binance_trades.arn]
    effect    = "Allow"
  }
}

resource "aws_iam_policy" "ecr_pull_push" {
  name   = "gh_actions_ecr_pull_push"
  policy = data.aws_iam_policy_document.data_policy.json
}

data "aws_iam_policy_document" "token" {
  statement {
    actions   = ["ecr:GetAuthorizationToken"]
    resources = ["*"]
    effect    = "Allow"
  }
}

resource "aws_iam_policy" "token" {
  name   = "gh_actions_token"
  policy = data.aws_iam_policy_document.token.json
}

resource "aws_iam_role_policy_attachment" "ecr_pull_push_attachment" {
  role       = aws_iam_role.gh_actions_role_oidc.name
  policy_arn = aws_iam_policy.ecr_pull_push.arn
}

resource "aws_iam_role_policy_attachment" "token_attachment" {
  role       = aws_iam_role.gh_actions_role_oidc.name
  policy_arn = aws_iam_policy.token.arn
}
