package br.com.ads.tasks.service;

import br.com.ads.tasks.model.Task;
import br.com.ads.tasks.repository.TaskRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class TaskService {
    
    @Autowired
    private TaskRepository taskRepository;
    
    public Task createTask(Task task) { return taskRepository.save(task); }
    
    public List<Task> listAllTasks() { return taskRepository.findAll(); }
    
    public Optional<Task> findTaskById(Long id) { return taskRepository.findById(id); }
    
    public Task updateTask(Long id, Task updatedTask) {
        Optional<Task> currentTask = taskRepository.findById(id);
        
        if (currentTask.isPresent()) {
        	Task task = currentTask.get();
        	task.setName(updatedTask.getName());
        	task.setDeliveryDate(updatedTask.getDeliveryDate());
        	task.setResponsibly(updatedTask.getResponsibly());
        	
            return taskRepository.save(task);
        }
        
        return null;
    }
    
    public boolean deleteTask(Long id) {
        if (taskRepository.existsById(id)) {
        	taskRepository.deleteById(id);
        	
            return true;
        }
        
        return false;
    }
}