# Identify the Advantes of Common Desgn Patterns

## Singleton

- Restricts classes to only being instantiated once during execution of the program
- Used for db connections, config values, constants, etc
- Requires a constructor method to enforce single-instantiation
- Not built directly into python so requires a bit of extra work

## Observer

- Dependent objects are updated or notified by one or more subject objects
- Objects react or respoond to events (used in UI systems)
- Two class types:
    - Subject: List of observers with methods to attach, detach, and notify observers
    - Observer: Has method to receive updates from subject
- Pros
	- Provides a loosly-coupled design between objects that interact
	- No need to modify the subject to add or remove observers
	- Subjects and observers can be re-used independently of each other
- Cons
	- Can introduce memory leaks

## Model View Controller

- Responsibilities delegated to three components:
    - Model: Stores data (db connector)
    - View: Displays data
    - Controller: Handles logic flow, user interactions, directs models and views
- Pros
	- Multiple developers can work on the same model, controller, and views simultaneously
	- Enables logical group of related actions
	- Models can have multiple views
- Cons
	- Can be more complex (introduces new layers of abstraction)
	- Developers need to be skilled in multiple technologies


