package br.com.ads.tasks.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import br.com.ads.tasks.model.Task;

@Repository
public interface TaskRepository extends JpaRepository<Task, Long> {}