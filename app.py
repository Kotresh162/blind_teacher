import streamlit as st
import streamlit.components.v1 as components
from wordfinder import build_default_trie

trie = build_default_trie()

st.title("Hello,It's your lovely Teacher")

button_to_key = {
    "1": "d",
    "2": "w",
    "3": "q",
    "4": "k",
    "5": "o",
    "6": "p",
    "Enter": "Enter"
}

if "input_string" not in st.session_state:
    st.session_state.input_string = ""
if "output_string" not in st.session_state:
    st.session_state.output_string = ""
if "enter_pressed" not in st.session_state:
    st.session_state.enter_pressed = False


decoded_string = trie.decode_input_string(st.session_state.input_string)
st.session_state.output_string = decoded_string


st.session_state.input_string = st.text_input("Input Box", value=st.session_state.input_string)


if st.session_state.enter_pressed:
    st.markdown(f"**Output Box:**\n\n**{st.session_state.output_string}**")
else:
    st.text_area("Output Box", value=st.session_state.output_string, height=100, disabled=True)


def append_key(label):
    key = button_to_key.get(label, "")
    if label in {"1", "2", "3", "4", "5", "6"}:
        st.session_state.input_string += key
        st.session_state.enter_pressed = False
    elif label == "Enter":
        st.session_state.enter_pressed = True


def render_buttons():
    rows = [
        [(0, "1"), (6, "6")],
        [(1, "2"), (5, "5")],
        [(2, "3"), (4, "4")],
        [(3, "Enter")],
    ]
    for row in rows:
        cols = st.columns(7)
        for pos, label in row:
            with cols[pos]:
                st.button(label, key=f"btn-{label}", on_click=append_key, args=(label,))

render_buttons()

components.html(
    """
    <script>
    document.addEventListener("keydown", function(e) {
        const keyMap = {
            "d": "1",
            "w": "2",
            "q": "3",
            "k": "4",
            "o": "5",
            "p": "6",
            "Enter": "Enter"
        };
        const btnLabel = keyMap[e.key];
        if (btnLabel) {
            const btn = window.parent.document.getElementById("btn-" + btnLabel);
            if (btn) btn.click();
        }
    });
    </script>
    """,
    height=0
)
