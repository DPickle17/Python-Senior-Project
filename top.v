`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: TCNJ Senior Project
// Engineer: Dylan Peck
// 
// Create Date: 11/07/2021 12:25:35 PM
// Design Name: 
// Module Name: FPGA_Handshake
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module FPGA_Handshake(
input clk, 
input reset_raw, 
input pi_hsk_raw, 
input wire [7:0] PMOD,    
output reg fpga_hsk
);

reg reset, reset_p1;
//making reset active high and flopping once
always @ (posedge clk)
begin
    reset_p1 <= ~reset_raw;
    reset <= reset_raw;
end
    
//double flop the handshake signals to avoid metastability issues
reg pi_hsk, pi_hsk_p1;

always @ (posedge clk)
begin
    pi_hsk_p1 <= pi_hsk_raw;
    pi_hsk <= pi_hsk_p1;
end

//Handshaking
always @ (posedge clk)
begin
    if(reset)
        fpga_hsk <= 1'b0;
    else
    begin
        fpga_hsk <= pi_hsk;   //one cycle delayed
    end
end

endmodule
