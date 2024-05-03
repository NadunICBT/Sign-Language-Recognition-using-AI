package com.example.SignLanguageDigitsDataset.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.SignLanguageDigitsDataset.Model.User;








public interface UserRepo extends JpaRepository<User, Long>{
	
	public User findByEmail(String email);

}
