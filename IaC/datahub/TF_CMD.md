

```sh
$ terrafrom init

$ terrafrom workspace list
$ terrafrom workspace select <env>
$ terrafrom workspace new <env>

$ terrafrom validate
$ terrafrom plan
$ terraform apply
$ terraform apply -auto-approve
$ terraform apply -var-file=$(terraform workspace show).tfvars -auto-approve

$ alias tfplan='terraform plan -var-file=$(terraform workspace show).tfvars'
$ alias tfapply='terraform apply -var-file=$(terraform workspace show).tfvars -auto-approve'
$ tfapply / tfplan -> will execute alias (only valid within an session)

$ terraform destroy
$ terraform destroy -auto-approve
$ terraform destroy -var-file=$(terraform workspace show).tfvars -auto-approve

```
