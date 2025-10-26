package com.uttaran.Movies.config; // Make sure this package name is correct!

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import org.springframework.web.filter.CorsFilter;

import java.util.List;

@Configuration
public class GlobalCorsConfig {

    @Value("${CORS_ALLOWED_ORIGIN}")
    private String allowedOrigin;

    @Bean
    public CorsFilter corsFilter() {
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        CorsConfiguration config = new CorsConfiguration();

        // This allows your frontend to send cookies/credentials
        config.setAllowCredentials(true);

        // This uses your Render environment variable
        config.setAllowedOrigins(List.of(allowedOrigin));

        // This allows all headers
        config.setAllowedHeaders(List.of("*"));

        // This allows all standard methods
        config.setAllowedMethods(List.of("GET", "POST", "PUT", "DELETE", "OPTIONS"));

        // This applies the config to ALL routes in your application
        source.registerCorsConfiguration("/**", config);

        return new CorsFilter(source);
    }
}