variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "ecr_repository_name" {
  description = "ECR repository name"
  type        = string
  default     = "event-flow-app"
}

variable "eks_cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "event-flow-cluster"
}

variable "node_instance_type" {
  description = "EKS node instance type"
  type        = string
  default     = "t3.medium"
}