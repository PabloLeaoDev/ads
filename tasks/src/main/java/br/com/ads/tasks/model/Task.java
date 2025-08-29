package br.com.ads.tasks.model;

import java.time.LocalDate;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "TASKS")
public class Task {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "TK_NAME", nullable = false)
    private String name;
    
    @Column(name = "TK_DELIVERY_DATE", nullable = false)
    private LocalDate deliveryDate;
    
    @Column(name = "TK_RESPONSIBLY", nullable = false)
    private String responsibly;
    
    public Task() {}
    
    public Task(String name, LocalDate deliveryDate, String responsibly) {
        this.name = name;
        this.deliveryDate = deliveryDate;
        this.responsibly = responsibly;
    }
    
    public Long getId() { return id; }
    
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    
    public void setName(String name) { this.name = name; }
    
    public LocalDate getDeliveryDate() { return deliveryDate; }
    
    public void setDeliveryDate(LocalDate deliveryDate) { this.deliveryDate = deliveryDate; }
    
    public String getResponsibly() { return responsibly; }
    
    public void setResponsibly(String responsibly) { this.responsibly = responsibly; }
}