import java.net.SocketException;
import java.io.IOException;
import java.net.*;

public class Rfc865UDPServer {
    static int port = 17;   // port for QOTD protocol
    static String QOTD = "A hungry fox jumped over a lazy cat!";    // what the local server will send back

    public static void main(String[] args) {
        // initialise the server socket
        DatagramSocket socket = null;
        try {
            socket = new DatagramSocket(port);  // set this socket to be using port 17
        }
        catch (SocketException e) {
            e.printStackTrace();
            System.exit(-1);
        }

        try {
            while (true) {
                // buffer for storing the received request from client
                byte[] buffer = new byte[512];
                // DatagramPack encapsulates the request message sent by client (to be stored in buffer)
                DatagramPacket request = new DatagramPacket(buffer, buffer.length);
                System.out.println("Waiting for response...");
                socket.receive(request);    // receives the request

                String requestContent = new String(buffer);     // pre-process the request message into String
                System.out.println("Received request: " + requestContent);
                
                InetAddress clientAddr = request.getAddress();  // gets the client IP address
                int clientPort = request.getPort();     // gets the client's port
                System.out.println("From client: " + clientAddr.getHostAddress());

                String replyContent = QOTD; // what gets replied back to client
                byte[] replyBuffer = replyContent.getBytes("UTF-8"); // stores the replied back message in replyBuffer
                System.out.println("Reply content: " + replyContent);

                // encapsulates the replied back message, which is found in replyBuffer
                DatagramPacket reply = new DatagramPacket(replyBuffer, replyBuffer.length, clientAddr, clientPort);
                System.out.println("Sending reply...");
                socket.send(reply); // sends the replied back message
                System.out.println("Reply has been sent");
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            socket.close();
        }
    }
}