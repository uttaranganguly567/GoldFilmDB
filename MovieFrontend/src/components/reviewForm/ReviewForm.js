import React from "react";
import { Button, Form } from "react-bootstrap";

const ReviewForm = ({handleSubmit, revText, labelText, defaultValue}) => {
    return (
        <div>
            <Form.Group className="mb3" controlId="exampleForm.ControlTextarea1">
                <Form.Label>{labelText}</Form.Label>
                <Form.Control ref={revText} as="textArea" rows={3} defaultValue={defaultValue} />
            </Form.Group>
            <Button variant="outline-info" onClick={handleSubmit}>Submit</Button>
        </div>
    )
}

export default ReviewForm