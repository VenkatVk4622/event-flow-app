output "ecr_repository_url" {
  description = "ECR repository URL"
  value       = aws_ecr_repository.event_flow.repository_url
}
