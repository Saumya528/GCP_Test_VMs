# GCP_Test_VMs
Testing out GCP for VM creation and Scaling Techniques
### **Overview**
This project focuses on deploying and configuring multiple Windows 10 Virtual Machines (VMs) using VirtualBox, creating a network connection between them, and deploying a microservice-based application. The system will include a RESTful API built with Node.js and a MongoDB database running on separate VMs, simulating a distributed environment.

### **System Requirements**
- An active Google Cloud Platform (GCP) account with billing enabled.
- Basic knowledge of GCP Console and Cloud Networking.
- (Optional) Google Cloud SDK for executing CLI commands.

### **Setup Steps**
1. **Log in to GCP**: Access the [Google Cloud Console](https://console.cloud.google.com/) and ensure billing is enabled.
2. **Create a GCP Project**: Go to the project dropdown, select **New Project**, set the project name, and ensure billing is enabled.
3. **Create a VM**: Go to **Compute Engine** > **VM Instances** and configure a virtual machine.
4. **Configure Auto-Scaling**: Set up an **Instance Template** and a **Managed Instance Group** with a CPU utilization threshold for auto-scaling.
5. **Implement Security**: Assign **IAM roles** for access control and define **firewall rules** to manage network traffic.
6. **Test Auto-Scaling**: Run a CPU-intensive task to raise CPU usage above 40% and observe auto-scaling in action.

### **Testing**
- Monitor auto-scaling in the **Instance Groups** section.
- Confirm that access restrictions based on **IAM roles** are functioning correctly.
- Test **firewall rules** by attempting to access the VM from unauthorized sources.

### **Conclusion**
This project demonstrates how to set up a scalable, secure cloud infrastructure on GCP. By implementing auto-scaling, IAM policies, and firewall rules, organizations can ensure cost-effective, secure, and highly available operations.

### **Conclusion**
This project demonstrates how to set up a scalable, secure cloud infrastructure on GCP. By implementing auto-scaling, IAM policies, and firewall rules, organizations can ensure cost-effective, secure, and highly available operations.
