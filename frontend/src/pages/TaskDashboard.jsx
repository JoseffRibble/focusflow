import React, { useEffect, useState } from "react";
import axios from "../utils/axiosInstance";

export default function TaskDashboard() {
  const [tasks, setTasks] = useState([]);
  const [form, setForm] = useState({
    title: "",
    short_description: "",
    long_description: "",
    due_date: "",
    priority: "MEDIUM",
  });
  const [error, setError] = useState("");
  const [editingTaskId, setEditingTaskId] = useState(null);
  const [editedTitle, setEditedTitle] = useState("");

  const token = localStorage.getItem("token");
  const headers = {
    "Content-Type": "application/json",
    Authorization: token ? `Bearer ${token}` : "",
  };

  const STATUS_LABELS = {
    OPEN: "Open",
    PENDING: "Pending",
    IN_REVIEW: "In Review",
    CLOSED: "Closed",
  };

  const fetchTasks = async () => {
    try {
      const response = await axios.get("/tasks/", {
        headers,
      });
      setTasks(response.data);
      setError("");
    } catch (err) {
      console.error("Fetch failed:", err.response?.data || err.message);
      setError("Failed to fetch tasks");
    }
  };

  const createTask = async () => {
    try {
      await axios.post("/tasks/", form, { headers });
      setForm({
        title: "",
        short_description: "",
        long_description: "",
        due_date: "",
        priority: "MEDIUM",
      });
      setError("");
      fetchTasks();
    } catch (err) {
      console.error("Create failed:", err.response?.data || err.message);
      setError("Failed to create task");
    }
  };

  const updateTaskStatus = async (taskId, newStatus) => {
    try {
      await axios.patch(
        `/tasks/${taskId}/`,
        { status: newStatus },
        { headers },
      );
      fetchTasks();
    } catch (err) {
      console.error("Status update failed:", err.response?.data || err.message);
      setError("Failed to update task status");
    }
  };

  const deleteTask = async (id) => {
    try {
      await axios.delete(`/tasks/${id}/`, { headers });
      fetchTasks();
    } catch (err) {
      console.error("Delete failed:", err.response?.data || err.message);
      setError("Failed to delete task");
    }
  };

  const startEdit = (task) => {
    setEditingTaskId(task.id);
    setEditedTitle(task.title);
  };

  const cancelEdit = () => {
    setEditingTaskId(null);
    setEditedTitle("");
  };

  const saveEdit = async (task) => {
    try {
      await axios.patch(
        `/tasks/${task.id}/`,
        { title: editedTitle },
        { headers },
      );
      setEditingTaskId(null);
      fetchTasks();
    } catch (err) {
      console.error("Save failed:", err.response?.data || err.message);
      setError("Failed to save title");
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const groupedTasks = tasks.reduce((acc, task) => {
    if (!acc[task.status]) acc[task.status] = [];
    acc[task.status].push(task);
    return acc;
  }, {});

  return (
    <div style={{ padding: "1rem" }}>
      <h2>Task Dashboard</h2>

      {/* Task creation form */}
      <div style={{ marginBottom: "1rem" }}>
        <input
          placeholder="Title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
        />
        <input
          placeholder="Short Description"
          value={form.short_description}
          onChange={(e) =>
            setForm({ ...form, short_description: e.target.value })
          }
        />
        <input
          placeholder="Long Description"
          value={form.long_description}
          onChange={(e) =>
            setForm({ ...form, long_description: e.target.value })
          }
        />
        <input
          type="date"
          value={form.due_date}
          onChange={(e) => setForm({ ...form, due_date: e.target.value })}
        />
        <select
          data-cy="create-priority"
          value={form.priority}
          onChange={(e) => setForm({ ...form, priority: e.target.value })}
        >
          <option value="LOW">LOW</option>
          <option value="MEDIUM">MEDIUM</option>
          <option value="HIGH">HIGH</option>
        </select>
        <button onClick={createTask}>Create Task</button>
      </div>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Kanban columns */}
      <div style={{ display: "flex", gap: "1rem" }}>
        {Object.keys(STATUS_LABELS).map((statusKey) => (
          <div
            key={statusKey}
            style={{
              flex: 1,
              border: "1px solid #ccc",
              padding: "0.5rem",
              borderRadius: "5px",
              backgroundColor: "#f9f9f9",
            }}
          >
            <h3 style={{ textAlign: "center" }}>{STATUS_LABELS[statusKey]}</h3>

            {groupedTasks[statusKey]?.map((task) => (
              <div
                data-cy={`task-${task.id}`}
                key={task.id}
                style={{
                  border: "1px solid #aaa",
                  borderRadius: "4px",
                  padding: "0.5rem",
                  marginBottom: "0.5rem",
                  backgroundColor: "#fff",
                }}
              >
                {editingTaskId === task.id ? (
                  <>
                    <input
                      type="text"
                      value={editedTitle}
                      onChange={(e) => setEditedTitle(e.target.value)}
                    />
                    <button onClick={() => saveEdit(task)}>Save</button>
                    <button onClick={cancelEdit}>Cancel</button>
                  </>
                ) : (
                  <>
                    <strong>{task.title}</strong>
                    <p style={{ margin: "0.3rem 0", fontSize: "0.9rem" }}>
                      {task.short_description || task.long_description}
                    </p>
                    <select
                      data-cy={`status-select-${task.id}`}
                      value={task.status}
                      onChange={(e) =>
                        updateTaskStatus(task.id, e.target.value)
                      }
                    >
                      {Object.keys(STATUS_LABELS).map((key) => (
                        <option key={key} value={key}>
                          {STATUS_LABELS[key]}
                        </option>
                      ))}
                    </select>
                    <div style={{ marginTop: "0.5rem" }}>
                      <button onClick={() => startEdit(task)}>Edit</button>
                      <button
                        data-cy={`delete-${task.id}`}
                        onClick={() => deleteTask(task.id)}
                        style={{ marginLeft: "0.5rem" }}
                      >
                        Delete
                      </button>
                    </div>
                  </>
                )}
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}
