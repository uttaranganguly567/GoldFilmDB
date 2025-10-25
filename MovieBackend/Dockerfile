# Use an official Java 22 runtime as a base image
FROM eclipse-temurin:22-jdk

# Set the working directory inside the container
WORKDIR /app

# Copy the Maven wrapper files
COPY .mvn/ .mvn
COPY mvnw .
COPY pom.xml .

# Add execute permissions to the mvnw script
RUN chmod +x mvnw

# Build the project dependencies (this layer is cached)
RUN ./mvnw dependency:go-offline

# Copy the rest of your source code
COPY src ./src

# Package the application, skipping tests
RUN ./mvnw clean package -DskipTests

# Set the port the container will expose
EXPOSE 8080

# Define the command to run your app
ENTRYPOINT ["java", "-jar", "target/Movies-0.0.1-SNAPSHOT.jar"]