package br.com.ads.tasks.controller;

import br.com.ads.tasks.model.Task;
import br.com.ads.tasks.service.TaskService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/task")
public class TaskController {
    
    @Autowired
    private TaskService taskService;
    
    @PostMapping
    public ResponseEntity<Task> createTsak(@RequestBody Task task) {
        Task newTask = taskService.createTask(task);
        
        return new ResponseEntity<>(newTask, HttpStatus.CREATED);
    }
    
    @GetMapping
    public ResponseEntity<List<Task>> listTask() {
        List<Task> tasks = taskService.listAllTasks();
        
        return new ResponseEntity<>(tasks, HttpStatus.OK);
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<Task> findById(@PathVariable Long id) {
        Optional<Task> task = taskService.findTaskById(id);
        
        return task.map(value -> new ResponseEntity<>(value, HttpStatus.OK))
                    .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<Task> updateTask(@PathVariable Long id, @RequestBody Task updatedTask) {
    	Task task = taskService.updateTask(id, updatedTask);
    	
        if (task != null)
            return new ResponseEntity<>(task, HttpStatus.OK);
        else
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteTask(@PathVariable Long id) {
        boolean removed = taskService.deleteTask(id);
        
        if (removed)
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        else
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
}
