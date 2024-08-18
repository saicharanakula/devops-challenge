provider "aws" {
  region = "ap-southeast-2"
}

# Create a security group to allow inbound traffic on port 80
resource "aws_security_group" "allow_http" {
  name        = "allow_http_traffic"
  description = "Allow HTTP traffic"

  ingress {
    description      = "Allow HTTP from anywhere"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "Allow SSH from anywhere"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    description      = "Allow all outbound traffic"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_http_traffic"
  }
}

resource "aws_instance" "app_server" {
  ami           = "ami-00aa03f67b64f75dd" # Amazon Linux 2 AMI
  instance_type = "t2.micro"
  security_groups = [aws_security_group.allow_http.name]
  key_name      = "devops"
  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo amazon-linux-extras install docker -y
              sudo service docker start
              sudo usermod -a -G docker ec2-user
              EOF

  tags = {
    Name = "python-api-server"
  }
}
