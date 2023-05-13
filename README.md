 
AirBnB Clone Project README
Welcome to the AirBnB clone project! This project is the first step towards building a full web application. Before starting, please read the AirBnB concept page to understand the project's requirements.

Project Description
The first step of the project is to create a command-line interpreter that will manage the AirBnB objects. This step is critical because it will be used for all other following projects, including HTML/CSS templating, database storage, API, front-end integration.

Project Tasks
The following tasks are linked and will help you create the AirBnB clone:

Put in place a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of your future instances.
Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
Create the first abstracted storage engine of the project: File storage.
Create all unittests to validate all our classes and storage engine.
What is a Command Interpreter?
A command interpreter is similar to the shell, but it is limited to a specific use-case. In our case, we want to be able to manage the objects of our project. With the command interpreter, you can:

Create a new object (e.g., a new User or a new Place)
Retrieve an object from a file, a database, etc.
Do operations on objects (count, compute stats, etc.)
Update attributes of an object
Destroy an object
How to Run the Command Interpreter
To run the command interpreter, follow these steps:

Clone the project repository to your local machine.
Navigate to the project directory.
Run the command interpreter using the following command: ./console.py.
Conclusion
This project is the first step towards building the AirBnB clone. By completing this project, you will have a solid foundation for all the following projects. If you have any questions, please refer to the AirBnB concept page or contact us for further assistance.
