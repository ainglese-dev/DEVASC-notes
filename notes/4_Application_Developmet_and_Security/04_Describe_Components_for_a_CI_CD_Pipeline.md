# Describe the Components of a CI/CD Pipeline

## CI: Continuous Integration

- Automating the combination of code changes from multiple contributors into a single code base
- Components:
  1. Source code control: Maintain a single repository per project and utilize branching for individual components
  2. Build automation
  3. Unit testing
  4. Branch merging
  5. Integration testing

## CD: Continuous Delivery

- Automating the delivery of IT services to users
- Components
  1. Central repository
  2. System testing
  3. Deployment (Ansible, Puppet, etc)
  4. User acceptance testing

## Example

1. Commit to git repository kicks off pipeline with hooks
2. Automated build process begins in Jenkins (compile if necessary, update db schema, generate configuration scripts)
3. Execute unit tests 
4. Deploy to test environment with e.g. Ansible
5. System testing is performed to validate deployment (can the web server talk to the db server, etc)
6. Deploy to user acceptance testing environment with e.g. Ansible
7. Deploy to production
