# Apply Concepts of Model-driven Programmability

## YANG

### Resources

- https://yangcatalog.org
  - Browse vendor-specific and industry-standard YANG modules
- https://netconfcentral.org
  - View raw YANG modules
- YANG Explorer
  - Python package used to connect to a device and browse available YANG modules for that device

## RESTCONF

## NETCONF

Send requests as RPCs embedded in XML

### RPC operations

#### get

Retrieve running configuration and device state information

#### get-config

Retrieve all or part of a specified configuration datastore

#### edit-conig

Edit a configuration datastore by creating, deleting, merging or replacing content

#### copy-config

Copy an entire configuration datastore to another configuration datastore

#### close-session

Request graceful terminatino of a NETCONF session

#### kill-session

Force the terminatino of a NETCONF session

#### lock

Lock an entire configuration datastore of a device

#### unlock

Release a configuration datastore lock previously obtained with the <lock> operation

#### validate

Checks the complete configuration for syntactical and semantic errors before applying the configuation to the device

#### commit

Sets the running configuration to the current contents of the candidate configuration

#### cancel-commit

Cancels an ongoing confirmed commit. MUST be issued on the same session that issued the confirmed commit if <persist-id> is not provided

#### discard-changes

Discards any uncommitted changes


