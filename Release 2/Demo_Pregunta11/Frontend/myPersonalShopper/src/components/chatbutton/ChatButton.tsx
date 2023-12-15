import "./ChatButton.css"
import ChatIcon from "../../assets/chat_icon.png"
//make the button have the chat icon

function ChatButton() {
  return (
    // add the chat icon in ../../assets/chat_icon.png to the button
    <button className="chatbutton_button">
      <img src={ChatIcon} alt="" />
    </button>
  )
}

export default ChatButton