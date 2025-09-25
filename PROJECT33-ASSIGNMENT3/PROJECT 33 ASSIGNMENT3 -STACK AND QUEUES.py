# =============================================================================
# PROJECT 33: STACKS AND QUEUES - RWANDA CONTEXT EXAMPLES
# Integrated code for all questions: Practicals, Challenges, and Reflections.
# Uses lists for stacks (simple) and deque for queues (efficient FIFO).
# =============================================================================

from collections import deque  # For efficient queue operations

# =============================================================================
# SECTION 1: STACK QUESTIONS - PRACTICALS
# =============================================================================

print("=== STACK PRACTICAL 1: UR Topics (Pop Once) ===")
# Practical (Rwanda): UR pushes ["Topic1", "Topic2", "Topic3"]. Pop once. Which is top?
stack_ur = []
stack_ur.append("Topic1")
stack_ur.append("Topic2")
stack_ur.append("Topic3")
print("After pushes:", stack_ur)

stack_ur.pop()  # Pop "Topic3"
print("After pop:", stack_ur)

top_topic = stack_ur[-1] if stack_ur else None
print("Top after pop:", top_topic)
print()  # Blank line for readability

print("=== STACK PRACTICAL 2: Remera Steps (Pop Twice) ===")
# Practical (Rwanda): In Remera, push ["Step1", "Step2", "Step3"]. Pop twice. What remains?
stack_remera = []
stack_remera.append("Step1")
stack_remera.append("Step2")
stack_remera.append("Step3")
print("After pushes:", stack_remera)

stack_remera.pop()  # First pop: "Step3"
print("After first pop:", stack_remera)
stack_remera.pop()  # Second pop: "Step2"
print("After second pop:", stack_remera)
print("Remaining in stack:", stack_remera)
print()

# =============================================================================
# SECTION 2: STACK CHALLENGE
# =============================================================================

print("=== STACK CHALLENGE: Reverse 'STACK' Using Stack (Step-by-Step) ===")
# Challenge: Reverse "STACK" using stack.
original = "STACK"
stack_reverse = []
result = []
print("Step 1 - Original string:", original)

# Push each character
for char in original:
    stack_reverse.append(char)
    print(f"Step 2 - Pushing '{char}': Stack = {stack_reverse}")

# Pop to build reverse
while stack_reverse:
    popped = stack_reverse.pop()
    result.append(popped)
    print(f"Step 3 - Popped '{popped}': Result so far = {''.join(result)} | Stack remaining = {stack_reverse}")

reversed_str = ''.join(result)
print("Step 4 - Final reversed string:", reversed_str)
print()

# =============================================================================
# SECTION 3: QUEUE QUESTIONS - PRACTICALS
# =============================================================================

print("=== QUEUE PRACTICAL 1: CHUK Patients (After 1 Served) ===")
# Practical (Rwanda): At CHUK, 5 patients queue. After 1 served, who is front?
queue_chuk = deque()
for i in range(1, 6):
    queue_chuk.append(f"Patient {i}")
print("Initial queue:", list(queue_chuk))

served_chuk = queue_chuk.popleft()  # Serve "Patient 1"
print("Served:", served_chuk)
print("Queue after serving 1:", list(queue_chuk))

front_patient = queue_chuk[0] if queue_chuk else None
print("Front after serving 1:", front_patient)
print()

print("=== QUEUE PRACTICAL 2: BK ATM Clients (Who Served First) ===")
# Practical (Rwanda): At BK ATM, 3 clients queue. Who is served first?
queue_atm = deque()
queue_atm.append("Client 1")
queue_atm.append("Client 2")
queue_atm.append("Client 3")
print("Initial queue:", list(queue_atm))

first_served = queue_atm.popleft()  # Serve "Client 1"
print("Served first:", first_served)
print("Remaining queue:", list(queue_atm))
print()

# =============================================================================
# SECTION 4: QUEUE CHALLENGE
# =============================================================================

print("=== QUEUE CHALLENGE: Queue vs Stack for Playlist Order ===")
# Challenge: Queue vs stack for playlist order. Which works better?
songs = ['Song1', 'Song2', 'Song3']

# Queue (FIFO) simulation
print("--- Queue (FIFO) Playlist Playback ---")
q_playlist = deque()
for song in songs:
    q_playlist.append(song)  # Enqueue at rear
print("Addition order:", list(q_playlist))
playback_order_q = []
while q_playlist:
    played = q_playlist.popleft()  # Dequeue from front
    playback_order_q.append(played)
print("Playback order:", playback_order_q)

# Stack (LIFO) simulation
print("--- Stack (LIFO) Playlist Playback ---")
s_playlist = []
for song in songs:
    s_playlist.append(song)  # Push to top
print("Addition order:", s_playlist)
playback_order_s = []
while s_playlist:
    played = s_playlist.pop()  # Pop from top
    playback_order_s.append(played)
print("Playback order:", playback_order_s)

# Comparison
print("--- Comparison ---")
print("Queue: Better for ordered playback (preserves addition sequence) - Order:", ' -> '.join(playback_order_q))
print("Stack: Poor for playlists (reverses order) - Order:", ' -> '.join(playback_order_s))
print("Recommendation: Use Queue for fair, sequential music playback.")
print()

# =============================================================================
# END OF CODE EXECUTION SECTIONS
# =============================================================================