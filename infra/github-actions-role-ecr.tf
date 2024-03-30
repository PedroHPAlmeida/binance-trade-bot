resource "aws_iam_policy" "ecr_pull_push" {
  name = "gh_actions_ecr_pull_push"

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowPushPull",
        "Effect" : "Allow",
        "Action" : [
          "ecr:BatchGetImage",
          "ecr:BatchCheckLayerAvailability",
          "ecr:CompleteLayerUpload",
          "ecr:GetDownloadUrlForLayer",
          "ecr:InitiateLayerUpload",
          "ecr:PutImage",
          "ecr:UploadLayerPart"
        ],
        "Resource" : "${aws_ecr_repository.ecr_repository_binance_trades.arn}"
      }
    ]
  })
}

resource "aws_iam_role" "gh_actions_role" {
  name = "gh_actions_role"
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "ec2.amazonaws.com" # Adicione o serviço IAM como principal
        },
        "Action" : [
          "sts:AssumeRole"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecr_pull_push_attachment" {
  role       = aws_iam_role.gh_actions_role.name
  policy_arn = aws_iam_policy.ecr_pull_push.arn
}
