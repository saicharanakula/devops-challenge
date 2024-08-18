provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-00aa03f67b64f75dd" # Amazon Linux 2 AMI
  instance_type = "t2.micro"
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
