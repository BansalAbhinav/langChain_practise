from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = '''
// Utility function to generate unique IDs
function generateId() {
  return Math.floor(Math.random() * 100000);
}

// A standalone function to format task status
function formatStatus(isCompleted) {
  return isCompleted ? "✅ Completed" : "⏳ Pending";
}

// Task class to represent individual tasks
class Task {
  constructor(title, description) {
    this.id = generateId();
    this.title = title;
    this.description = description;
    this.isCompleted = false;
    this.createdAt = new Date();
  }

  completeTask() {
    this.isCompleted = true;
  }

  getDetails() {
    return `${this.title} - ${this.description} [${formatStatus(this.isCompleted)}]`;
  }
}

// TaskManager class to manage multiple tasks
class TaskManager {
  constructor() {
    this.tasks = [];
  }

  addTask(title, description) {
    const newTask = new Task(title, description);
    this.tasks.push(newTask);
    console.log(`Task "${title}" added successfully.`);
  }

  completeTask(id) {
    const task = this.tasks.find(t => t.id === id);
    if (task) {
      task.completeTask();
      console.log(`Task "${task.title}" marked as completed.`);
    } else {
      console.log("Task not found.");
    }
  }

  listTasks() {
    if (this.tasks.length === 0) {
      console.log("No tasks available.");
      return;
    }
    console.log("Your Tasks:");
    this.tasks.forEach(task => {
      console.log(`${task.id}: ${task.getDetails()}`);
    });
  }

  deleteTask(id) {
    const index = this.tasks.findIndex(t => t.id === id);
    if (index !== -1) {
      console.log(`Task "${this.tasks[index].title}" deleted.`);
      this.tasks.splice(index, 1);
    } else {
      console.log("Task not found.");
    }
  }
}

// Example usage
const manager = new TaskManager();
manager.addTask("Learn LangChain", "Study text splitters and embeddings");
manager.addTask("Build AI Agent", "Use LangGraph for multi-step workflows");
manager.listTasks();

const firstTaskId = manager.tasks[0].id;
manager.completeTask(firstTaskId);

manager.listTasks();
manager.deleteTask(firstTaskId);
manager.listTasks();

'''

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JS,
    chunk_size=100,
    chunk_overlap=0,

)

chunks= splitter.split_text(text)

print(len(chunks))
print(chunks[1])
