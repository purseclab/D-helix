import re

call_message ="%15 = call i32 (%struct.AVIOContext*, %struct.AVIOContext*, i64, i64) bitcast (i32 (three_dot)* @avio_rb32 to i32 (%struct.AVIOContext*, %struct.AVIOContext*, i64, i64)*)(%struct.AVIOContext* %7, %struct.AVIOContext* %8, i64 %11, i64 %14)"

arglist =  re.search("bitcast (.+?)\*\)\((.*)",call_message).group(2)
#print(arglist)

new_message = "i64 %414, i32 2, i8* getelementptr inbounds ([23 x i8], [23 x i8]* @.str.13, i32 0, i32 0), i8* getelementptr inbounds ([61 x i8], [61 x i8]* @.str.16, i32 0, i32 0), i64 %420, i64 %428, i64 %436, i64 %437"
for i in range(new_message.count('getelementptr')):
    replacement = re.search("getelementptr inbounds \((.+?)\)",new_message).group(1)
    new_message = new_message.replace("("+replacement+")",'three_dot')
    print(new_message)
