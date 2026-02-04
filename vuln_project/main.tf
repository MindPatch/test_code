# Vulnerable Terraform configuration for testing Checkov

provider "aws" {
  region = "us-east-1"
}

# VULN: S3 bucket without encryption
resource "aws_s3_bucket" "data" {
  bucket = "my-insecure-bucket"
  acl    = "public-read"  # VULN: Public access
}

# VULN: S3 bucket without versioning
resource "aws_s3_bucket" "logs" {
  bucket = "my-log-bucket"
}

# VULN: Security group with overly permissive ingress
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Web security group"

  # VULN: SSH open to the world
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # VULN: All ports open
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # VULN: Unrestricted egress
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# VULN: RDS instance without encryption
resource "aws_db_instance" "database" {
  identifier           = "mydb"
  engine               = "mysql"
  instance_class       = "db.t2.micro"
  allocated_storage    = 20
  username             = "admin"
  password             = "password123"  # VULN: Hardcoded password
  publicly_accessible  = true           # VULN: Publicly accessible
  skip_final_snapshot  = true
  storage_encrypted    = false          # VULN: No encryption
}

# VULN: EC2 instance without encryption
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"

  # VULN: No IMDSv2 requirement
  metadata_options {
    http_tokens = "optional"
  }

  # VULN: Public IP assigned
  associate_public_ip_address = true

  # VULN: No monitoring enabled
  monitoring = false
}

# VULN: IAM policy with wildcard permissions
resource "aws_iam_policy" "admin" {
  name = "admin-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "*"
        Resource = "*"
      }
    ]
  })
}

# VULN: EBS volume without encryption
resource "aws_ebs_volume" "data" {
  availability_zone = "us-east-1a"
  size              = 100
  encrypted         = false
}

# VULN: CloudWatch log group without encryption
resource "aws_cloudwatch_log_group" "app" {
  name = "/app/logs"
  # Missing: kms_key_id for encryption
}
