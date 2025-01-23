# Azure Terraform Project

This project is designed to provision Azure infrastructure using Terraform. It utilizes Azure Blob Storage for the backend configuration to manage the state of the infrastructure.

## Project Structure

- **main.tf**: The main configuration file where Azure resources are defined.
- **variables.tf**: Contains the input variables for the Terraform configuration.
- **outputs.tf**: Defines the output values that will be displayed after the infrastructure is created.
- **terraform.tfvars**: Contains the specific values for the variables declared in `variables.tf`.
- **backend.tf**: Configures Azure Blob Storage as the backend for Terraform state management.
- **README.md**: Documentation for the project.

## Getting Started

1. **Prerequisites**:
   - Install Terraform.
   - Set up an Azure account.

2. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd azure-terraform-project
   ```

3. **Configure Backend**:
   Update the `backend.tf` file with your Azure Blob Storage details.

4. **Initialize Terraform**:
   Run the following command to initialize the Terraform configuration:
   ```bash
   terraform init
   ```

5. **Plan the Deployment**:
   Generate an execution plan:
   ```bash
   terraform plan
   ```

6. **Apply the Configuration**:
   Deploy the infrastructure:
   ```bash
   terraform apply
   ```

7. **Outputs**:
   After the deployment, check the output values defined in `outputs.tf`.

## Cleanup

To destroy the resources created by Terraform, run:
```bash
terraform destroy
```

## License

This project is licensed under the MIT License.